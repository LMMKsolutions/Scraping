# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:34:32 2024

@author: Max
"""

import tensorflow_text as text
import tensorflow_hub as hub
import tensorflow as tf

from news_scraper import sentences


text_input = [sentences[4]];
preprocessor = hub.KerasLayer("https://kaggle.com/models/tensorflow/bert/TensorFlow2/en-uncased-preprocess/3")


encoder_inputs = preprocessor(text_input)
encoder = hub.KerasLayer("https://www.kaggle.com/models/tensorflow/bert/TensorFlow2/bert-en-uncased-l-12-h-768-a-12/2",trainable=True)

outputs = encoder(encoder_inputs)


pooled_output = outputs["pooled_output"]      # [batch_size, 768].
sequence_output = outputs["sequence_output"]  # [batch_size, seq_length, 768].

print(sequence_output)
