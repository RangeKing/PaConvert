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

obj = APIBase("torch.Tensor.nanmedian")


# TODO: paddle has bug to fix
def _test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([1.4907, float('nan'), 1.0593, 1.5696])
        result = input.nanmedian()
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[1.4907, float('nan'), 1.0593, 1.5696], [1.4907, float('nan'), 1.0593, 1.5696]])
        result = input.nanmedian(1)
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        unsupport=True,
        reason="paddle does not return index when dim is specified",
    )


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[1.4907, 1.0593, 1.5696], [1.4907, 1.0593, 1.5696]])
        result = input.nanmedian(1, keepdim=True)
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        unsupport=True,
        reason="paddle does not return index when dim is specified",
    )


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[1.4907, float('nan'), 1.0593, 1.5696], [1.4907, float('nan'), 1.0593, 1.5696]])
        result = input.nanmedian(dim=1, keepdim=True)
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        unsupport=True,
        reason="paddle does not return index when dim is specified",
    )


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([1, 4, 6])
        result = input.nanmedian(0)
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        unsupport=True,
        reason="paddle does not return index when dim is specified",
    )
