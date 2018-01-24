#ifndef _DEMO_MODEL_COMPRESSION_COMPRESSION_H
#define _DEMO_MODEL_COMPRESSION_COMPRESSION_H

#include <vector>

namespace research_demo {

/*
 * Reference:
 *   Deep compression: Compressing deep neural networks with pruning,
 *       trained quantizatoin and huffman coding
 *   A Survey of Model Coompression and Acceleration for Deep Neural Networks
 *
 * Model Quantization
 *
 * Basic idea:
 *   Remove parameters which are not crucial to the model performance.
 */
struct CSR {
  std::vector<float> buffer;
  std::vector<std::pair<size_t /*offset*/, float /*value*/>> pos;
};

void Prune(float *buffer, size_t size, prune_ratio);

class BufferPrune {
public:
  BufferPrune(float prune_ratio) : prune_ratio_(prune_ratio) {}

  void Prune();

  void ToCSR();

private:
  float prune_ratio_;
};

} // namespace research_demo

#endif
