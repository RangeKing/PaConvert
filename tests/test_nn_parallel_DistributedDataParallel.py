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

import textwrap

from apibase import APIBase

obj = APIBase("torch.nn.parallel.DistributedDataParallel")


# Distributed package doesn't have NCCL built in
def _test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import os
        os.environ["USE_LIBUV"] = "0"
        torch.distributed.init_process_group(
            "nccl",
            init_method="tcp://127.0.0.1:23456",
            rank=0,
            world_size=1
        )
        model = torch.nn.Linear(1, 1, bias=False).cuda()
        model = torch.nn.parallel.DistributedDataParallel(model)
        result=True
        """
    )
    obj.run(pytorch_code, ["result"])


def _test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import os
        os.environ["USE_LIBUV"] = "0"
        torch.distributed.init_process_group(
            "nccl",
            init_method="tcp://127.0.0.1:23456",
            rank=0,
            world_size=1
        )
        model = torch.nn.Linear(1, 1, bias=False).cuda()
        model = torch.nn.parallel.DistributedDataParallel(model,device_ids=[0])
        result=True
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        torch.distributed.init_process_group(
            "nccl",
            init_method="tcp://127.0.0.1:23456",
            rank=0,
            world_size=1
        )
        model = torch.nn.Linear(1, 1, bias=False).cuda()
        model = torch.nn.parallel.DistributedDataParallel(model,device_ids=[0],output_device=0)
        result=True
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        unsupport=True,
        reason="paddle not support the parameter",
    )
