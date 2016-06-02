# ckanext-dara

CKAN extension that integrates the [da|ra metadata
schema](http://www.da-ra.de/en/technical-information/doi-registration/#c880) and enables
registration of DOIs at [da|ra](http://www.da-ra.de/en/home/). It has been developed for
the [EDaWaX](http://http://www.edawax.de/) project at the [ZBW](http://zbw.eu) (German
National Library of Economics) and is now actively used for the CKAN based RDM platform
[ZBW Journal Data Archive](http://journaldata.zbw.eu).


## General
CKAN offers only a kind of general and limited set of metadata for datasets (like title,
description, author), that does not reflect any common schema. You can, nevertheless, add
arbitrary fields via the webinterface for each dataset. But that’s not schema based. The
approach of CKAN here is to avoid extensive metadata forms, that might restrict the
usability of the portal, and also not to specialise on certain types or categories of
data, like, you name it, research data. Dedicated research data applications like
Dataverse do have an advantage here. Dataverse’s metadata forms are based on the
well-known and very extensive DDI schema. CKAN is not originally a research data
management tool, and the lack of decent metadata schema support is one point where this
hurts. However, this more general approach as well as the plugin infrastructure enables us
to customise the dataset forms, add specific (meta‑)data, and to guarantee compatibility
with a given schema. `ckanext-dara` does that for the [da|ra metadata schema](http://www.da-ra.de/en/technical-information/doi-registration/#c880).

`ckanext-dara` has been developed with two principles in mind:

1.  *make metadata input and DOI registration as easy as possible* <br /> The ZBW Journal
Data Archive is intended for editors and authors of scientific journals, who like to
publish the research data on which their article is based. Those persons neither have time
nor motivation to fill in 100+ metadata fields before they can upload their data.
`ckanext-dara` therefore provides only a small subset of the original da|ra metadata
schema.
2.  *provide as much metadata as necessary* <br />
Metadata is, however, necessary, even for authors themselves. It's important for the
findability of research data as well as for the linking to other objects, and for
reproducabilty of data. We are therefore also trying to receive metadata from other
services. This is exemplarily realised for the author metadata fields, that retrieve data
from ORCID or GND. The author fields also implement a feature orginally not found in CKAN.
It enables field repeating, which simply means you can add as many authors as you like.


## Requirements
Tested with CKAN 2.4.

Required Python packages (all installed with the package):

-   [lxml](https://pypi.python.org/pypi/lxml/3.5.0) (for XML validation)
-   [toolz](https://pypi.python.org/pypi/toolz/0.7.4) (a library that eases functional programming with Python)


Installation
------------

Clone this repository into your CKAN src folder and install it the usual way
`pip install -e path/to/repo` or `python setup.py` inside your virtualenv.


## Configuration

If you want to use the DOI registration service at da|ra you must provide the
credentials and your registered DOI prefix in your `development.ini`:

```ini
ckanext.dara.user = <your da|ra account ID>
ckanext.dara.password = <your da|ra account password>
ckanext.dara.doi_prefix = <your prefix, e.g. 10.12345>
```

For developing and testing purposes you can also use the da|ra testserver.
However, you'll also have to provide credentials:

```ini
ckanext.dara.use_testserver = true #default: false
ckanext.dara.demo.user = <da|ra testaccount>
ckanext.dara.demo.password = <da|ra testpassword>
```

## Schema
All metadata fields are based on `ckanext.dara.schema`. Fields are namedtuples
and processed in plugin.py. Widgets are constructed as objects and processed by Jinja
macros.

## Tests
Warning: tests are far from being perfect or complete.

Run the tests the usual way with nosetests. You should however provide the da|ra
testserver credentials in test.ini or tests for DOI registration will fail.

## License
This extension is open and licensed under the GNU General Public License (GPL)
v3.0. Its full text may be found at: http://www.gnu.org/licenses/gpl.html

## Contact
Please use GitHub issues for filing any bug or problem. If you have further questions please contact h.bunke@zbw.eu.
