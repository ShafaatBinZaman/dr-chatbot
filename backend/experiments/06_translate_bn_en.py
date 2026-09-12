import sys
from transformers import pipeline
bn2en = pipeline("translation", model="csebuetnlp/banglat5_nmt_bn_en")
en2bn = pipeline("translation", model="csebuetnlp/banglat5_nmt_en_bn")
bn = "আমার গতকাল থেকে জ্বর এবং শরীর ব্যথা" if len(sys.argv)<2 else " ".join(sys.argv[1:])
en = bn2en(bn)[0]["translation_text"]
bn_back = en2bn(en)[0]["translation_text"]
print({"bn":bn,"en":en,"roundtrip_bn":bn_back})
