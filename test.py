import slate3k as slate

with open('d.pdf', 'rb') as f:
    extracted_text = slate.PDF(f)
print(extracted_text)