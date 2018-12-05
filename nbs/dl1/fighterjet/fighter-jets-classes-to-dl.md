# Classes

-------------------
2018-12-02 15:14:26

urls = Array.from(document.querySelectorAll('.rg_di .rg_meta')).map(el=>JSON.parse(el.textContent).ou);
window.open('data:text/csv;charset=utf-8,' + escape(urls.join('\n')));

### American
* f22   -   f 22 raptor fighter
* f14   -   f 14 tomcat fighter
* f15c  -   f 15c eagle fighter jet
* f15e  -   f 15e strike eagle fighter jet
* f16   -   f 16 fighter jet
* f18   -   f/a-18c hornet fighter jet aircraft -"f/a-18e/f"
* f18e+ -   f/a-18e/f super hornet fighter jet aircraft -"f/a-18a/c"
* f35   -   f 35 jsf lightning 2
* f4    -   f4 phantom fighter jet

### European
* typhoon   -   eurofighter typhoon jet
* rafale    -   dassault rafale fighter jet
* jas39     -   jas 39 gripen fighter jet
* tornado # -   panavia tornado jet

### Russian
* mig29         -   mig 29 fighter jet
* su27 (35)     -   sukhoi su 27 flanker fighter jet
* su30          -   sukhoi su 30 flanker fighter jet
* mig25         -   mig25 fighter jet
* mig31         -   mig31 fighter jet interceptor
* mig21         -   mig 21 fighter jet
* mig23         -   миг 23 flogger fighter jet
* su57          -   су 57 -"f-35" истребитель
* su17 (20/22)  -   su 22m4 su 17 20 22 fitter fighter jet
* su34 #        -   су 34
* su24 #        -   су 24
* su25 #        -   су 25
* mig27 #       -   миг 27

### Other
* j20   -   歼-20


I think I can use multi-label classification to address the issue of aircraft types not included in the dataset. So by adding a 'fighter' class to all fighter jets, when the model will still recognize a fighter it's never seen before as a fighter. This can be extended to a general 'aircraft' class as well, to differntiate fighters from other airframes.

'Fighter' is loosely taken to have a crew of 1-2 and includes ground-attack aircraft.