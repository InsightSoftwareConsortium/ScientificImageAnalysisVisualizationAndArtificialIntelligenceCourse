================================================
Biomedical Image Analysis and Visualization: ITK
================================================
Kitware, Carrboro, North Carolina, USA
======================================

.. image:: https://mybinder.org/badge.svg
  :target: https://mybinder.org/v2/gh/KitwareMedical/CourseInBiomedicalImageAnalysisVisualizationAndArtificialIntelligence/master

Instructors:

- Matt McCormick, PhD

.. image:: data/kitware-logo.png
  :alt: Kitware
  :width: 400px

.. image:: data/itk-logo.png
  :alt: ITK
  :width: 500px


The `Insight Toolkit (ITK) (www.itk.org) <https://www.itk.org>`_
has become a standard in academia and industry for
medical image analysis. In recent years, the ITK community has
focused on providing programming interfaces to ITK from Python and JavaScript
and making ITK available via leading applications such as Slicer and ImageJ.
In this course, we present best practices for taking advantage of ITK in your
imaging research and commercial products. We demonstrate how to utilize the algorithms
in ITK and the multitude of ITK extensions that are freely available on the web.

Run the Tutorial
----------------

There are many ways to run these tutorials.

On the Web, with Binder
^^^^^^^^^^^^^^^^^^^^^^^

To run the notebooks in
`MyBinder <https://mybinder.readthedocs.io/en/latest/>`_,
simply `click this link <https://mybinder.org/v2/gh/KitwareMedical/CourseInBiomedicalImageAnalysisVisualizationAndArtificialIntelligence/master>`_.

Locally, with Docker
^^^^^^^^^^^^^^^^^^^^

First, `install Docker <https://docs.docker.com/install/>`_, if not already
available.

Next, clone the repository::

  git clone https://github.com/KitwareMedical/CourseInBiomedicalImageAnalysisVisualizationAndArtificialIntelligence
  cd CourseInBiomedicalImageAnalysisVisualizationAndArtificialIntelligence

Then, build and run the Docker image::

  ./build.sh
  ./run.sh

Paste the URL presented in the terminal in your web browser.

Locally, with Python from Python.org or a System Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, `install Python
<https://www.python.org/downloads/release/python-365/>`_,
if not already available.

Next, install the required dependencies::

   python -m pip install jupyter matplotlib numpy scipy ipywidgets scikit-learn cookiecutter
   python -m pip install --upgrade itk itk-texturefeatures
   python -m pip install itkwidgets

Then, clone the repository::

  git clone https://github.com/KitwareMedical/CourseInBiomedicalImageAnalysisVisualizationAndArtificialIntelligence.git
  cd CourseInBiomedicalImageAnalysisVisualizationAndArtificialIntelligence

And start Jupyter::

  python -m jupyter notebook

Locally, with Conda
^^^^^^^^^^^^^^^^^^^

First, `install MiniConda <https://conda.io/miniconda.html>`_ or Anaconda, if
not already available.

Next, install the required dependencies::

   conda install -c conda-forge jupyter matplotlib numpy scipy ipywidgets scikit-learn cookiecutter
   python -m pip install --upgrade itk itk-texturefeatures
   python -m pip install itkwidgets

Then, clone the repository::

  git clone https://github.com/KitwareMedical/CourseInBiomedicalImageAnalysisVisualizationAndArtificialIntelligence.git
  cd CourseInBiomedicalImageAnalysisVisualizationAndArtificialIntelligence

And start Jupyter::

  python -m jupyter notebook
