import json
import os

from transformers import AutoConfig as AC, AutoModelForCausalLM as AM
from .mpt import MPTConfig, MPTForCausalLM


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


class AutoConfig():
    def from_pretrained(path, *args, **kwargs):
        config = load_json(os.path.join(path, "config.json"))

        archs = config.get("architectures")
        if archs and archs[0] == "MPTForCausalLM":
            return MPTConfig.from_pretrained(path, *args, **kwargs)

        return AC.from_pretrained(path, *args, **kwargs)


class AutoModelForCausalLM():
    def from_config(config, *args, **kwargs):
        archs = config.architectures
        if archs and archs[0] == "MPTForCausalLM":
            return MPTForCausalLM.from_config(config, *args, **kwargs)

        return AM.from_config(config, *args, **kwargs)

    def from_pretrained(path, *args, **kwargs):
        config = load_json(os.path.join(path, "config.json"))

        archs = config.get("architectures")
        if archs and archs[0] == "MPTForCausalLM":
            return MPTForCausalLM.from_pretrained(path, *args, **kwargs)

        return AM.from_pretrained(path, *args, **kwargs)
