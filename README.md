# Lexical-and-Syntax-analyzer

<b>Design a lexical and LR parser for the following code</b>

int main()

begin

     int count=1;
     
     while(n>1) 
     
     begin    
     
          count=count+1;
          
          n=n/2;
          
     end while 
     
     return count;
     
end 

<b>The LR1 grammar is :</b>

S'->S

S->datatype MAINFUNCTION

MAINFUNCTION->MAIN begin NL STMTS end NL

MAIN->main ( ) NL

STMTS->STMT STMTS

STMTS->STMT

STMT->DECLARE SC NL

STMT->EXPRESSION SC NL

STMT->WHILESTMT 

STMT->RETURNSTMT SC NL

DECLARE->datatype DECVARS

DECVARS->DECVAR

DECVARS->DECVAR comma DECVARS

DECVAR->id

DECVAR-> id equalsto number

EXPRESSION->id equalsto VARNUM

EXPRESSION->id equalsto VARNUM operator VARNUM

VARNUM->id

VARNUM->number

WHILESTMT->while(id condition VARNUM)WTSTMT

WTSTMT->NL begin NL STMTS end while NL

RETURNSTMT->return VARNUM


<b>Can be rewritten as :</b>

a->datatype

A->MAINFUNC

b->begin

B->MAIN

c->NL

C->STMTS

d->end

D->STMT

e->main

E->DECLARE

f->(

F->EXPRESSION

g->)

G->WHILESTMT

h->sc

H->RETURNSTMT

i->comma

I->DECVARS

j->id

J->DECVAR

k->equalsto

K->VARNUM

l->number

L->WSTMT

m->operator

n->while

o->condition

p->return

<b>New grammar:</b>

S' -> S

S -> a A

A -> B b c C d c

B -> e f g c

C -> D C

C -> D

D -> E h c

D -> F h c

D -> G

D -> H h c

E -> a I

I -> J

I -> J i I

J -> j

J -> j k l

F -> j k K

F -> j k K m K

K -> j

K -> l

G -> n f j o K g L

L -> c b c C d n c

H -> p K

<b>String to be parsed:</b>

a e f g c b c a j k l h c n f j o l g c b c j k j m l h c j k j m l h c d n c p j h c d c
