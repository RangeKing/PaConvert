# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 

set +x

echo "Insalling gpu version torch, which has been installed in Dockerfile"
python -c "import torch; print('torch version information:' ,torch.__version__)"

echo "Insalling develop gpu version paddle"
python -m pip uninstall -y paddlepaddle
python -m pip uninstall -y paddlepaddle-gpu
python -m pip install -U --pre paddlepaddle-gpu -i https://www.paddlepaddle.org.cn/packages/nightly/cu118/
python -c "import paddle; print('paddle version information:' , paddle.__version__); commit = paddle.__git_commit__;print('paddle commit information:' , commit)"

echo "Insalling paconvert requirements"
python -m pip install -r ../../requirements.txt

echo "Converting torch code to paddle"
python ../../paconvert/main.py -i . -o /tmp/paddle_dist --log_level "DEBUG"

export CUDA_VISIBLE_DEVICES=0,1
netstat -tulnp | grep :29500 | awk '{print $7}' | cut -d/ -f1 | xargs kill -9 2> nul

check_error=0
if [ $# -gt 0 ] ; then
    item=$1
    cmd1="torchrun --nproc_per_node=2 ${item}"
    cmd2="python -m paddle.distributed.launch /tmp/paddle_dist/${item}"
    python run_and_compare.py "$cmd1" "$cmd2"; check_error=$?
    echo "Exit code:" $check_error
    exit $check_error
fi

failed_tests=()
test_list=`ls *.py | grep -v run_and_compare.py`
for item in $test_list; do
    cmd1="torchrun --nproc_per_node=2 ${item}"
    cmd2="python -m paddle.distributed.launch /tmp/paddle_dist/${item}"
    python run_and_compare.py "$cmd1" "$cmd2"; tmp_check_error=$?
    if [ $tmp_check_error -ne 0 ]; then
        check_error=1
        failed_tests+=("$item")
    fi
done

echo "Failed tests:"
for item in $failed_tests; do
    echo "$item"
done
echo "Exit code:" $check_error
exit $check_error
