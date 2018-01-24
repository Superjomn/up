from __future__ import division
import random
import numpy as np


class QuantizationEncoder(object):
    def __init__(self, num_buckets):
        self.floor = None
        self.ceil = None
        self.num_buckets = num_buckets

    def learn(self, data):
        self.floor = np.min(data) if self.floor is None else min(
            self.floor, np.min(data))
        self.ceil = np.max(data) if self.ceil is None else max(
            self.ceil, np.max(data))

    def quantize(self, data):
        '''
        data should be a np.array of shape 1, n
        '''
        span = (self.ceil - self.floor) / self.num_buckets
        for i in len(data):
            v = data[i]
            if v < self.floor: v = self.floor
            if v > self.ceil: v = self.ceil

            offset = (v - self.floor) / span
            data[i] = offset


class Sampler:
    def __init__(self, num_samples):
        self.num_records = 0
        self.num_samples = num_samples
        self.samples = np.zeros(num_samples)

    def add(self, value):
        '''
        value: scalar
        '''
        if self.num_records < self.num_samples:
            self.samples[self.num_records] = v
        else:
            to_sample = random.random() < self.num_samples / self.num_records
            if to_sample:
                offset = random.randint(0, self.num_samples)
                self.samples[offset] = value


class BinaryEncoder:
    def __init__(self, prune_ratio):
        self.prune_ratio = prune_ratio
        self.threshold = None
        self.sampler = Sampler(10000)

    def learn(self, data):
        for v in data:
            self.sampler.add(v)

    def gen_threshold(self):
        offset = self.prune_ratio * self.sampler.num_samples
        np.partition(self.sampler.samples, offset)
        self.threshold = self.sampler.samples[offset]

    def encode(self, data):
        '''
        data should be a list
        '''
        for i in range(len(data)):
            data[i] = 0 if data[i] < self.threshold else 1
