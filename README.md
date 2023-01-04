# What's the bug?
When comparing a failed snapshot test on an object without a custom `__repr__` (i.e. relies on syrupy's serialiser), PyCharm incorrectly displays the actual output as the default `__repr__` (e.g. `...Mansion object at 0xBEEF2020`) instead of what syrupy serialises it to (e.g. `Mansion(rooms=[Room(...)])`).

# How to reproduce the bug

1. checkout this repo
2. create a virtualenv within and `pip install syrupy`
3. find the singular test within the run configurations and notice that it fails.
4. in the failed test output, scroll to the clickable '\<Click to see difference\>' text: ![image](https://user-images.githubusercontent.com/62700647/210490066-9e4dc3c5-013a-4d2a-93fd-f0740395066a.png)
5. click that text and you should get a Comparison Failure interface like this: ![image](https://user-images.githubusercontent.com/62700647/210490207-2158aefd-8d9c-4104-a5cd-aa1391d56cea.png)
6. This is wrong because when I run `pytest --snapshot-update`, it updates the snapshot like this. This is roughly what I should see in the Comparison Failure window.![image](https://user-images.githubusercontent.com/62700647/210490506-957bb941-1b4f-4748-9512-ef1377f6e6d0.png)
