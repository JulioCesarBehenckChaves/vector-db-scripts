# vector-db-scripts

## google scholar

[Ref](https://stackoverflow.com/questions/62938110/does-google-scholar-have-an-api-available-that-we-can-use-in-our-research-applic)

### How to get Google Scholar metadata given by keywords?

#### pip install inUbuntu 20.04

```bash
sudo apt update
sudo apt install python3-pip -y
sudo apt install python3.10-venv -y
```



[Ref scrape-google-scholar-py](https://github.com/dimitryzub/scrape-google-scholar-py#example-usage-custom-backend)

Compilar da fonte.

```python
git clone https://github.com/dimitryzub/scrape-google-scholar-py.git \
&& cd scrape-google-scholar-py \
&& python3 -m venv env && source env/bin/activate \
&& pip3 install -r requirements.txt
```

Precisa instalar o Chrome.

[Link](https://www.edivaldobrito.com.br/como-instalar-o-google-chrome-no-ubuntu-20-04-via-repositorio-oficial/)

```bash
sudo apt install x11-apps
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
sudo apt-get update
sudo apt install google-chrome-stable -y
```

Rodando exemplo

```python
python3 example_usage.py
```
