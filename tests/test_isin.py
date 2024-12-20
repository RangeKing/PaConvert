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

import textwrap

from apibase import APIBase

obj = APIBase("torch.isin")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.isin(torch.tensor([[1, 2], [3, 4]]), torch.tensor([2, 3]))
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.isin(torch.tensor([[1, 2], [3, 4]]), torch.tensor([2, 3]), assume_unique=True)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.isin(torch.tensor([[1, 2], [3, 4]]), torch.tensor([2, 3]), invert=True)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.isin(elements=torch.tensor([[1, 2], [3, 4]]), test_elements=torch.tensor([2, 3]), assume_unique=True, invert=True)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        elemnts = torch.tensor([[1, 2], [3, 4]])
        test_elemnts = torch.tensor([2, 3])
        result = torch.isin(assume_unique=True, invert=True, test_elements=test_elemnts, elements=elemnts)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([0., 1., 2.]*20).reshape([20, 3])
        test_x = torch.tensor([0., 1.]*20)
        correct_result = torch.isin(x, test_x, assume_unique=False)
        incorrect_result = torch.isin(x, test_x, assume_unique=True)
        """
    )
    obj.run(pytorch_code, ["correct_result", "incorrect_result"])
