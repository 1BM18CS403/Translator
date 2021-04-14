from easynmt import EasyNMT
model_name = "m2m_100_418M"
model = EasyNMT(model_name)

def translate(src, trg, src_text):
    translations = model.translate(src_text, source_lang=src, target_lang=trg)
    return translations
