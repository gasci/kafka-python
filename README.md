# kafka-python

### Apple Silicon Pre-requisites (Confluent-kafka):

```bash
git clone https://github.com/edenhill/librdkafka.git
cd librdkafka
./configure --install-deps
brew install  openssl zstd pkg-config
./configure
make
sudo make install 
```