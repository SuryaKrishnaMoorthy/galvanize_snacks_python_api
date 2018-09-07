- router.get('/', snacksController.index)

- router.get('/:id', snacksController.show)

- router.post('/', snacksController.create)

- router.patch('/:id', snacksController.update)

- router.delete('/:id', snacksController.destroy)


- router.post('/', reviewsController.create)

- router.patch('/:revId', reviewsController.update)

- router.delete('/:revId', reviewsController.destroy)

- router.get('/featured', snacksController.featured)
