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
import os

import torch
import torch.distributed as dist

dist.init_process_group(backend="nccl")
rank = dist.get_rank()
torch.cuda.set_device(rank)

if rank == 0:
    data1 = torch.tensor([0, 1]).cuda()
    data2 = torch.tensor([2, 3]).cuda()
else:
    data1 = torch.tensor([4, 5]).cuda()
    data2 = torch.tensor([6, 7]).cuda()
dist.reduce_scatter(
    data1, [data1, data2], op=dist.ReduceOp.SUM, group=None, async_op=False
)

if rank == 0:
    print(data1)
    torch.save(data1, os.environ["DUMP_FILE"])
