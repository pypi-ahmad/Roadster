import numpy as np
from skimage import exposure
from skimage import transform


def vote_on_image(models, image, threshold=0.9):
    image = transform.resize(image, (32, 32))
    image = exposure.equalize_adapthist(image, clip_limit=0.1)
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)
    voting_dict = {}
    for voter in models:
        preds = voter.predict(image)
        top = np.argsort(-preds, axis=1)
        for i, vote in enumerate(top[0][:3]):
            if preds[0][vote] > threshold:
                if vote not in voting_dict:
                    voting_dict[vote] = preds[0][vote]
                else:
                    voting_dict[vote] += preds[0][vote]

    winner = None

    if len(voting_dict) > 0:
        winner = max(voting_dict, key=voting_dict.get)

    return winner
