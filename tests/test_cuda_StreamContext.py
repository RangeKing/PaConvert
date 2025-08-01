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

import paddle
import pytest
from apibase import APIBase

obj = APIBase("torch.cuda.StreamContext")


@pytest.mark.skipif(
    condition=not paddle.device.is_compiled_with_cuda(),
    reason="can only run on paddle with CUDA",
)
def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        s1 = torch.cuda.Stream(device=0)
        a = torch.zeros(10, 10, device='cuda')
        b = torch.zeros(10, 10, device='cuda')
        with torch.cuda.StreamContext(stream=s1):
            result = a + b
        """
    )
    obj.run(pytorch_code, ["result"])


@pytest.mark.skipif(
    condition=not paddle.device.is_compiled_with_cuda(),
    reason="can only run on paddle with CUDA",
)
def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        s1 = torch.cuda.Stream(device=0)
        a = torch.zeros(10, 10, device='cuda')
        b = torch.zeros(10, 10, device='cuda')
        with torch.cuda.StreamContext(s1):
            result = a + b
        """
    )
    obj.run(pytorch_code, ["result"])
