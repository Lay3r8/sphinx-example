# This file is used to auto-generate the documentation for the files under ../scripts
echo "Removing all files under source/* and _build/*"
rm -rf source/* _build/*

echo "Generating source files..."
sphinx-apidoc -f -o source/ ../scripts

echo "Creating HTML docs..."
make html

echo "Done"
