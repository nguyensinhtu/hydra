# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from omegaconf import MISSING


@dataclass
class IncompatibleDataclassArgConf:
    _target_: str = "tests.test_modules.IncompatibleDataclassArg"
    num: int = MISSING
    # [passthrough] incompat: Incompatible
