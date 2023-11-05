import hashlib

username_trial = b"GOUGH"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = ""
key_part_static2_trial = "}"

encoded_dynamic = hashlib.sha256(username_trial).hexdigest()
key_part_dynamic1_trial = encoded_dynamic[4] + encoded_dynamic[5] + encoded_dynamic[3] + encoded_dynamic[6] + encoded_dynamic[2] + encoded_dynamic[7] + encoded_dynamic[1] + encoded_dynamic[8]
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
print(key_full_template_trial)