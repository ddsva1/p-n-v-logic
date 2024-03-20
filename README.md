# p-n-v-logic
### python_imp_no_firewall
based off https://blog.cryptographyengineering.com/2023/10/06/to-schnorr-and-beyond-part-1/
#### shared knowledge:
g: generator of some large cyclic group of prime order q
p: large non-secret prime number that 'defines a finite field'
q:
knowledge of constant (g^m)mod(p) as prover's public key

#### peggy's knowledge:
m: secret key
b: random integer picked specifically for this conversation


#### definitions:
finite field:
a set of numbers that is finite.
operations of multiplication, addition, subtraction and division are defined and satisfy certain basic rules.
a common example is the set of all integers mod p (a prime) applied.