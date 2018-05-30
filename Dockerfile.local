FROM jupyter/scipy-notebook:1fbaef522f17
MAINTAINER Matt McCormick <matt.mccormick@kitware.com>

RUN conda install --yes --quiet -c damianavila82 rise
RUN python -m pip install itk itk-ultrasound itk-texturefeatures
RUN python -m pip install itkwidgets && \
  python -m jupyter nbextension install --py --sys-prefix itkwidgets && \
  python -m jupyter nbextension enable --py --sys-prefix itkwidgets
RUN mkdir -p $HOME/.jupyter && \
  echo "c.NotebookApp.iopub_data_rate_limit=1e22" >> $HOME/.jupyter/jupyter_notebook_config.py
RUN python -m pip install cookiecutter

ADD data/kitware-logo-small.png /home/jovyan/.jupyter/custom/logo.png
ADD data/jupyter-custom.css /home/jovyan/.jupyter/custom/custom.css
USER root
RUN chown -R $NB_USER:users /home/jovyan/.jupyter
