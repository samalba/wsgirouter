from setuptools import setup

version = '0.4'

setup(
        name='WSGIRouter',
        version=version,
        description=('Tiny library for WebOb to manage URL and Request '
            'routing correctly without many dependencies'),
        keywords='wsgi request web http',
        author='Samuel Alba',
        author_email='sam.alba@gmail.com',
        url='https://github.com/samalba/wsgirouter',
        license='MIT',
        packages=['wsgirouter'],
        package_dir={'wsgirouter': '.'},
        install_requires=['webob >= 1.1.1'],
        zip_safe=True
        )
