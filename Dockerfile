FROM python:3

RUN apt-get update
#. pip => PHP でいう composer 、Rubyでいう gem みたいなもの
RUN pip install --upgrade pip
#. jupyterlab => ブラウザ上で動作する対話型実行環境
RUN python -m pip install jupyterlab


# RUN pip install pandas
# RUN pip install requests
# RUN pip install selenium
# RUN pip install beautifulsoup4




# Set working directory
WORKDIR /app



# Run JupyterLab on container start
CMD ["jupyter-lab", "--ip", "0.0.0.0", "--allow-root", "-b", "localhost"]
