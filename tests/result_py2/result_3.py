('test_precisely',
 [('F821', 13, 22, "undefined name 'LdaModel'",
   'lda = LdaModel(corpus=mm, id2word=id2word, num_topics=100, distributed=True)\n'),
  ('F821', 13, 38, "undefined name 'mm'",
   'lda = LdaModel(corpus=mm, id2word=id2word, num_topics=100, distributed=True)\n'),
  ('F821', 13, 50, "undefined name 'id2word'",
   'lda = LdaModel(corpus=mm, id2word=id2word, num_topics=100, distributed=True)\n')],
 {'logical lines': 2, 'physical lines': 2, 'tokens': 23})
