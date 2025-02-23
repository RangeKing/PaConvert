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

obj = APIBase("torch.Tensor.addbmm_")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([[[4., 5., 6.], [1., 2., 3.]]])
        b = torch.tensor([[[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]]])
        input = torch.tensor([[1., 2., 3.], [4., 5., 6.]])
        result = input.addbmm_(a, b)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([[[4., 5., 6.], [1., 2., 3.]]])
        b = torch.tensor([[[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]]])
        input = torch.tensor([[1., 2., 3.], [4., 5., 6.]])
        result = input.addbmm_(a, b, beta=3)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([[[4., 5., 6.], [1., 2., 3.]]])
        b = torch.tensor([[[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]]])
        input = torch.tensor([[1., 2., 3.], [4., 5., 6.]])
        result = input.addbmm_(batch1=a, batch2=b, beta=3, alpha=3)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[1., 2., 3.], [4., 5., 6.]])
        result = input.addbmm_(batch1=torch.tensor([[[4., 5., 6.], [1., 2., 3.]]]), batch2=torch.tensor([[[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]]]), beta=3, alpha=3)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([[[4., 5., 6.], [1., 2., 3.]]])
        b = torch.tensor([[[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]]])
        input = torch.tensor([[1., 2., 3.], [4., 5., 6.]])
        result = input.addbmm_(beta=3, alpha=3, batch2=b, batch1=a)
        """
    )
    obj.run(pytorch_code, ["result"])
