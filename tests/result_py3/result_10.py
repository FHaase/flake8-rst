('test_precisely',
 [('F821', 6, 10, "undefined name 'LdaModel'", 'lda = LdaModel(corpus=mm, id2word=id2word,\n'),
  ('F821', 6, 26, "undefined name 'mm'", 'lda = LdaModel(corpus=mm, id2word=id2word,\n'),
  ('F821', 6, 38, "undefined name 'id2word'", 'lda = LdaModel(corpus=mm, id2word=id2word,\n'),
  ('F821', 7, 47, "undefined name 'distribution_required'",
   '               num_topics=100, distributed=distribution_required)\n'),
  ('F821', 10, 10, "undefined name 'LdbModel'",
   'ldb = LdbModel(corpus=mm, id2word=id2word, num_topics=100, distributed=True)\n'),
  ('F821', 10, 26, "undefined name 'mm'",
   'ldb = LdbModel(corpus=mm, id2word=id2word, num_topics=100, distributed=True)\n'),
  ('F821', 10, 38, "undefined name 'id2word'",
   'ldb = LdbModel(corpus=mm, id2word=id2word, num_topics=100, distributed=True)\n')],
 {'logical lines': 6, 'physical lines': 7, 'tokens': 51})
