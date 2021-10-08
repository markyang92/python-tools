from distutils.core import setup, Extension

setup(  
        name="cpy",
        ext_modules=[
            Extension("cpy", ["cpy.c"], include_dirs=['.'],)
        ]
)


