# Copyright (c) 2025 PaddlePaddle Authors. All Rights Reserved.
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

obj = APIBase("torch._foreach_trunc")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        tensors = [torch.tensor([0.34, 5.76, 0.73]), torch.tensor([0.5, 1.0])]
        result = torch._foreach_trunc(tensors)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        tensors = [torch.tensor([0.34, 6.34, 0.73]), torch.tensor([0.5, 8.0])]
        result = torch._foreach_trunc(self=tensors)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch._foreach_trunc(self = [torch.tensor([0.34, 2.46, 0.73]), torch.tensor([0.5, 3.0])])
        """
    )
    obj.run(pytorch_code, ["result"])
