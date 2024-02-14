/*=========================================================================

 *  Copyright NumFOCUS
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *         https://www.apache.org/licenses/LICENSE-2.0.txt
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *
 *=========================================================================*/

#include "itkPipeline.h"
#include "itkInputImage.h"
#include "itkOutputImage.h"
#include "itkSupportInputImageTypes.h"

template <typename TImage>
int MedianImageFilter(itk::wasm::Pipeline &pipeline, const TImage *inputImage)
{
  using ImageType = TImage;

  pipeline.get_option("input-image")->required()->type_name("INPUT_IMAGE");

  using OutputImageType = itk::wasm::OutputImage<ImageType>;
  OutputImageType outputImage;
  pipeline.add_option("output-image", outputImage, "The output image")->required()->type_name("OUTPUT_IMAGE");

  unsigned int radius = 1;
  pipeline.add_option("-r,--radius", radius, "Kernel radius in pixels");

  ITK_WASM_PARSE(pipeline);

  // Pipeline code goes here

  return EXIT_SUCCESS;
}

template <typename TImage>
class PipelineFunctor
{
public:
  int operator()(itk::wasm::Pipeline &pipeline)
  {
    using ImageType = TImage;

    using InputImageType = itk::wasm::InputImage<ImageType>;
    InputImageType inputImage;
    pipeline.add_option("input-image", inputImage, "The input image");

    ITK_WASM_PRE_PARSE(pipeline);

    typename ImageType::ConstPointer image = inputImage.Get();
    return MedianImageFilter<ImageType>(pipeline, image);
  }
};

int main(int argc, char *argv[])
{
  itk::wasm::Pipeline pipeline("median-image-filter", "Computes an image where a given pixel is the median value of the the pixels in a neighborhood about the corresponding input pixel.", argc, argv);

  return itk::wasm::SupportInputImageTypes<PipelineFunctor,
                                           uint8_t,
                                           float>::Dimensions<2U, 3U>("input-image", pipeline);
}
