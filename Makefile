default: all

J=jupyter nbconvert  --ExecutePreprocessor.kernel_name=python3 --ExecutePreprocessor.timeout=0 --allow-errors --execute
JN=date; $(J) --to notebook --inplace
JH=date; $(J) --to html

all:
	#pandoc notebooks/31_synthetic.ipynb --resource-path=notebooks -s --extract-media=content/images  -t markdown -o content/31_synthetic.md
	pandoc notebooks/31_synthetic.ipynb --resource-path=notebooks --extract-media=content/images  -t markdown -o content/31_synthetic.md

clean:
	rm -fr ./figures

install_local:
	python3 -m pip install --user -r requirements.txt

install_global:
	python3 -m pip install -r requirements.txt
