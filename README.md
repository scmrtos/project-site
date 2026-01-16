# scmRTOS Documentation Project

## General

There are two variants of documentation:

  1. Static site for online access at https://scmrtos.github.io.
  2. PDF manuals for offline usage.

## Create Online Documentation

To create online documentation site, there two repositories are needed:

  1. One with documentation sources (Markdown).
  2. And one more for site itself.

Make sure the repos are:

```
├── ...
├── ...
├── project-site
├── ...
└── scmrtos.github.io
```

Complete all tasks on `project-site`. Perform pushing `master` branch to github.com:

```
cd project-site
...
git push origin master
```

Go to `scmrtos.github.io`.  Activate python virtual environment:

```
source <path-to-venv>/bin/activate
```

Invoke the above command:
```
mkdocs gh-deploy --config-file ../project-site/mkdocs.yml --remote-branch master
```

## MkDocs Markdown to PDF Converion

To build PDF documentation launch `script/md2pdf.py`. This commant creates `build` directory and performs Markdown to PDF converion for English and Russian documentation variants. 

To clean build clear the target directory and then make build:

```
rm -rf build && script/md2pdf.py
```

or with automatic viewing result

```
rm -rf build && script/md2pdf.py && atril build/scmrtos-en.pdf
```

where `atril` is PDF viewer, can be used any suitable one.
