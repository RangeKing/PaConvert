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


class cudaGetDeviceProperitesAPI(APIBase):
    def compare(
        self,
        name,
        pytorch_result,
        paddle_result,
        check_value=True,
        check_shape=True,
        check_dtype=True,
        check_stop_gradient=True,
        rtol=1.0e-6,
        atol=0.0,
    ):
        assert pytorch_result == paddle_result or isinstance(
            paddle_result, paddle.framework.core._gpuDeviceProperties
        )


obj = cudaGetDeviceProperitesAPI("torch.cuda.get_device_properties")


@pytest.mark.skipif(
    condition=not paddle.device.is_compiled_with_cuda(),
    reason="can only run on paddle with CUDA",
)
def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.cuda.get_device_properties(0)
        name = result.name
        major = result.major
        minor = result.minor
        total_memory = result.total_memory
        multi_processor_count = result.multi_processor_count
        """
    )
    obj.run(
        pytorch_code,
        ["name", "major", "minor", "total_memory", "multi_processor_count"],
    )


@pytest.mark.skipif(
    condition=not paddle.device.is_compiled_with_cuda(),
    reason="can only run on paddle with CUDA",
)
def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.cuda.get_device_properties(device="cuda:0")
        name = result.name
        major = result.major
        minor = result.minor
        total_memory = result.total_memory
        multi_processor_count = result.multi_processor_count
        """
    )
    obj.run(
        pytorch_code,
        ["name", "major", "minor", "total_memory", "multi_processor_count"],
    )


@pytest.mark.skipif(
    condition=not paddle.device.is_compiled_with_cuda(),
    reason="can only run on paddle with CUDA",
)
def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.cuda.get_device_properties(torch.device("cuda:0"))
        name = result.name
        major = result.major
        minor = result.minor
        total_memory = result.total_memory
        multi_processor_count = result.multi_processor_count
        """
    )
    obj.run(
        pytorch_code,
        ["name", "major", "minor", "total_memory", "multi_processor_count"],
    )


@pytest.mark.skipif(
    condition=not paddle.device.is_compiled_with_cuda(),
    reason="can only run on paddle with CUDA",
)
def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        t = torch.tensor([1,2,3]).cuda()
        result = torch.cuda.get_device_properties(device=torch.device("cuda:0"))
        name = result.name
        major = result.major
        minor = result.minor
        total_memory = result.total_memory
        multi_processor_count = result.multi_processor_count
        """
    )
    obj.run(
        pytorch_code,
        ["name", "major", "minor", "total_memory", "multi_processor_count"],
    )


@pytest.mark.skipif(
    condition=not paddle.device.is_compiled_with_cuda(),
    reason="can only run on paddle with CUDA",
)
def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.cuda.get_device_properties(device="cuda:0")
        name = result.name
        major = result.major
        minor = result.minor
        total_memory = result.total_memory
        multi_processor_count = result.multi_processor_count
        """
    )
    obj.run(
        pytorch_code,
        ["name", "major", "minor", "total_memory", "multi_processor_count"],
    )


@pytest.mark.skipif(
    condition=not paddle.device.is_compiled_with_cuda(),
    reason="can only run on paddle with CUDA",
)
def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        idx = 0
        result = torch.cuda.get_device_properties(idx)
        name = result.name
        major = result.major
        minor = result.minor
        total_memory = result.total_memory
        multi_processor_count = result.multi_processor_count
        """
    )
    obj.run(
        pytorch_code,
        ["name", "major", "minor", "total_memory", "multi_processor_count"],
    )


@pytest.mark.skipif(
    condition=not paddle.device.is_compiled_with_cuda(),
    reason="can only run on paddle with CUDA",
)
def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        device = "cuda:1"
        result = torch.cuda.get_device_properties(device)
        name = result.name
        major = result.major
        minor = result.minor
        total_memory = result.total_memory
        multi_processor_count = result.multi_processor_count
        """
    )
    obj.run(
        pytorch_code,
        ["name", "major", "minor", "total_memory", "multi_processor_count"],
    )


@pytest.mark.skipif(
    condition=not paddle.device.is_compiled_with_cuda(),
    reason="can only run on paddle with CUDA",
)
def test_case_8():
    pytorch_code = textwrap.dedent(
        """
        import torch
        device=torch.device("cuda:0")
        result = torch.cuda.get_device_properties(device)
        name = result.name
        major = result.major
        minor = result.minor
        total_memory = result.total_memory
        multi_processor_count = result.multi_processor_count
        """
    )
    obj.run(
        pytorch_code,
        ["name", "major", "minor", "total_memory", "multi_processor_count"],
    )


@pytest.mark.skipif(
    condition=not paddle.device.is_compiled_with_cuda(),
    reason="can only run on paddle with CUDA",
)
def test_case_9():
    pytorch_code = textwrap.dedent(
        """
        import torch
        cond = True
        device= "cuda:1" if cond else "cuda:0"
        result = torch.cuda.get_device_properties(device=device)
        name = result.name
        major = result.major
        minor = result.minor
        total_memory = result.total_memory
        multi_processor_count = result.multi_processor_count
        """
    )
    obj.run(
        pytorch_code,
        ["name", "major", "minor", "total_memory", "multi_processor_count"],
    )


@pytest.mark.skipif(
    condition=not paddle.device.is_compiled_with_cuda(),
    reason="can only run on paddle with CUDA",
)
def test_case_10():
    pytorch_code = textwrap.dedent(
        """
        import torch
        cond = True
        device= "cuda:1" if cond else "cuda:0"
        result = torch.cuda.get_device_properties(device=torch.device(device))
        name = result.name
        major = result.major
        minor = result.minor
        total_memory = result.total_memory
        multi_processor_count = result.multi_processor_count
        """
    )
    obj.run(
        pytorch_code,
        ["name", "major", "minor", "total_memory", "multi_processor_count"],
    )
