# fastapi-with-machine-learning
contoh sederhana penggunaan model machine learning dengan fastapi python

dataset : titanic

algoritma/model : K nearest neighbors

linked machine learning project : [repo](https://github.com/aronei44/belajar-machine-learning)

## instalasi

- clone repo ini

```
git clone https://github.com/aronei44/fastapi-with-machine-learning.git
cd fastapi-with-machine-learning
```

- jalankan instalasi package

```
py -m pip install -r requirements.txt
```

- jalankan aplikasi

```
uvicorn main:app --reload
```
cek http://127.0.0.1:8000/docs

## contoh data
```py
{
  name: "udin" # nama. bebas
  pclass :  3 # class tiket : 1, 2, 3 (vvip, vip, common)
  sex : "male" # male, female
  age : 20 # umur. bebas
  sibsp : 1 # jumlah saudara dan pasangan. bebas
  parch : 1 # jumlah ortu dan anak. bebas
  fare : 200 # harga tiket (vvip > 180, vip > 140, common < 140)
}
```
