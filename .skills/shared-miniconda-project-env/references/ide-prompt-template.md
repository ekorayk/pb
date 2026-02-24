# IDE Prompt Templates

Use these templates verbatim when delegating setup to another IDE AI assistant.

## Template 1 - Generic Project

```text
Eger Miniconda yolu verilmediyse once sor: "Hangi Miniconda yolunu kullanmami istersin?"
Bu projede paylasilan Miniconda kurulumu olarak <MINICONDA_ROOT> kullan.
Proje ici izole env olustur: <PROJECT_ROOT>\\.conda\\envs\\<ENV_NAME>.
Conda package cache: <PROJECT_ROOT>\\.conda\\pkgs.
Pip cache: <PROJECT_ROOT>\\.pip-cache.
<PROJECT_ROOT>\\.condarc olustur ve CONDARC'i bu dosyaya ayarla.
Base ortamina kurulum yapma.
Tum kurulum/indirme/build artefactlari yalnizca <PROJECT_ROOT> altinda kalsin.
```

## Template 2 - Strict Generic Variant

```text
Eger Miniconda yolu verilmediyse once sor: "Hangi Miniconda yolunu kullanmami istersin?"
Bu gorevde Miniconda yolu sabit: <MINICONDA_ROOT>.
Proje yolu sabit: <PROJECT_ROOT>.
Conda env: <PROJECT_ROOT>\\.conda\\envs\\<ENV_NAME>
Conda cache: <PROJECT_ROOT>\\.conda\\pkgs
Pip cache: <PROJECT_ROOT>\\.pip-cache
<PROJECT_ROOT>\\.condarc olustur ve CONDARC'i bu dosyaya ayarla.
Base ortamina kurulum yapma.
Bu projeyle ilgili tum indirme/kurulum dosyalari sadece <PROJECT_ROOT> altinda olacak.
```
