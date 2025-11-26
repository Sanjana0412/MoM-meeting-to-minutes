from datasets import load_dataset, load_from_disk
import os

# 1. Load the AMI dataset (IHM config)
ds = load_dataset("edinburghcstr/ami", "ihm")

print(ds)   # to check splits

# 2. Save it into your raw folder
save_path = r"data/raw/AMI"
os.makedirs(save_path, exist_ok=True)

ds.save_to_disk(save_path)

print(f"\n✅ AMI dataset saved to: {save_path}")

