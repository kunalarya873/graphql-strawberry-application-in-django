# GraphQL Strawberry Application in Django

## Overview

This project demonstrates how to integrate GraphQL Strawberry with Django to build a powerful and flexible API. GraphQL allows clients to request only the data they need, making it ideal for modern web applications.

## Features

- **Type-Safe Schemas**: Define your data models with type safety.
- **Efficient Data Fetching**: Clients can query exactly what they need.
- **Django Integration**: Leverage Django's ORM and admin features.
- **Easy Setup**: Quick installation and configuration.

## Prerequisites

- Python 3.6+
- Django 3.0+
- Basic knowledge of GraphQL

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/kunalarya873/graphql-strawberry-application-in-django.git
   cd graphql-strawberry-application-in-django
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**:

   ```bash
   python manage.py migrate
   ```

4. **Start the development server**:

   ```bash
   python manage.py runserver
   ```

## Usage

Once the server is running, you can access the GraphQL endpoint at:

```
http://localhost:8000/graphql/
```

Use tools like [GraphiQL](https://github.com/graphql/graphiql) or [Postman](https://www.postman.com/) to test your queries.

## Example Query

Here’s a simple example of how to query data:

```graphql
{
  allItems {
    id
    name
    description
  }
}
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please reach out via [kunalarya873](https://github.com/kunalarya873/) or open an issue in the repository.