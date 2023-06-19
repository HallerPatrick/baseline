
from transformers import (AutoConfig, AutoModel, AutoModelForCausalLM,
                          AutoModelForSequenceClassification, AutoTokenizer)

from gpt_neox.configuration_gpt_neox import CGPTNeoXConfig
from gpt_neox.modeling_gpt_neox import (
        CGPTNeoXForCausalLM, CGPTNeoXModel)

AutoConfig.register("cgpt_neox", CGPTNeoXConfig)
# AutoTokenizer.register("gpt_ngme", GPTNGMETokenizer)
AutoModel.register(CGPTNeoXConfig, CGPTNeoXModel)
AutoModelForCausalLM.register(CGPTNeoXConfig, CGPTNeoXForCausalLM)
