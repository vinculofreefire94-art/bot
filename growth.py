referrals = {}

def add_ref(referrer_id):
    if referrer_id not in referrals:
        referrals[referrer_id] = 0

    referrals[referrer_id] += 1
    return referrals[referrer_id]
