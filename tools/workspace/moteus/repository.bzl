# -*- python -*-

# Copyright 2018-2019 Josh Pieper, jjp@pobox.com.
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

load("//tools/workspace:github_archive.bzl", "github_archive")

def moteus_repository(name):
    github_archive(
        name = name,
        repo = "mjbots/moteus",
        commit = "892773daffe27f946e010782cd4223c7d4e53636",
        sha256 = "23d9ae153a44ac666e0ab0b61556c1cab4a398c78cdecc6be353cd2b934c15b6",
    )
