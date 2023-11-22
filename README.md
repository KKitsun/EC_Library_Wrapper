# Написання обгортки для зручного використання бібліотеки, що працює з алгеброю на еліптичних кривих
## Завдання
### Написати обгортки до бібліотечних функцій
Напишіть функції-обгортки для обраної вами бібліотеки, що дадуть вам змогу виконувати основні перетворення з точками ЕК зручним для вас чином. Приклади структури точки і методів для роботи з точками наведені нижче.
```
type ECPoint struct {
	X *big.Int
	Y *big.Int
}

func BasePointGGet() (point ECPoint) {} 		//G-generator receiving
func ECPointGen(x, y *big.Int) (point ECPoint) {}	//ECPoint creation
func IsOnCurveCheck(a ECPoint) (c bool) {} 		//DOES P ∈ CURVE?
func AddECPoints(a, b ECPoint) (c ECPoint) {} 	//P + Q
func DoubleECPoints(a ECPoint) (c ECPoint) {} 	//2P	
func ScalarMult(k big.Int, a ECPoint) (c ECPoint) {}	//k * P
func ECPointToString(point ECPoint) (s string) {} 	//Serialize point
func StringToECPoint(s string) (point ECPoint) {} 	//Deserialize point
func PrintECPoint(point ECPoint) {} 			//Print point
```
### Перевірити коректність роботи перетворень
З використанням власних функцій-обгорток реалізуйте перевірку коректності роботи бібліотеки та відповідних обгорток. Для цього напишіть обчислення простого рівняння. Приклад рівняння і псевдокоду наведений нижче.
```
k*(d*G) = d*(k*G)

ECPoint G = BasePointGGet()
big.Int k = SetRandom(256)
big.Int d = SetRandom(256)

H1 = ScalarMult(d, G)
H2 = ScalarMult(k, H1)

H3 = ScalarMult(k, G)
H4 = ScalarMult(d, H3)

bool result = IsEqual(H2, H4)
```

## Інструкція щодо запуска коду
Код розроблено з використанням Python 3.10.7. Для запуску коду необхідно мати встановлений Python відповідної або більш нової версії та прописати наступну консольну команду у директорії файлу:
```python
python .\EC_Kitsun.py
```
## Приклад визову програми та результату виконання програми
Приклад визову програми та результату виконання програми зображено на рисунку нижче. Також даний скріншот можна знайти в репозиторії.

![Code_exectuion_example](https://github.com/KKitsun/EC_Library_Wrapper/blob/master/ExecuteExmpl.PNG)

При обчислені першого рівняння паралельно перевіряється генерація базової точки, скалярного добутку, перевірка чи належить точка кривій, функцій серіалізації та десеріалізації, функція виводу точки у консоль, функція перевірки рівності двох точок. У другому рівнянні перевіряється сума точок та подвоєння(2P).
