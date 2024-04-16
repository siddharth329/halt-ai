# Halt.AI

One stop solution for organizations to manage the use of Generative AI chatbots like Gemini and ChatGPT by their employees.

## Installation

System Requirements:

`Python 3.12.0`

`NodeJS v21.7.2`

Clone the project using the GitUrl

```bash
git clone <git-url>
```

#### Installing the requirements for the `backend`.

```bash
cd backend
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install necessary requirements.

```bash
pip install -r requirements.txt
```

Now we will configure `ngrok` to create an `https` URL for our backend so that chrome extension could make API requests to it.
Chrome does not allow to make requests to `http` based local host servers for security reasons. SignUp on the `ngrok` website at [https://ngrok.com/](<(https://ngrok.com/)>) and replace the `<auth-token>` by the auth token provided by website in the following command.

```bash
ngrok config add-authtoken <auth-token>
```

In a new terminal with base directory as the project folder, run the following command to create an `https` secured URL using ngrok which will be used in the frontend to make the requests to the backend.

```bash
./ngrok.exe http http://127.0.0.1:8000
```

Before Initialization, we need to create and configure the following `.env` file inside the `<PROJECT_FOLDER>\backend\backend` folder.

```bash
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_KEY=

FACEBOOK_CLIENT_ID=
FACEBOOK_CLIENT_SECRET=

CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=

API_KEY_XXX=GEMINI_API_KEY
```

Now we can setup the database by following commands.

```bash
python ./manage.py makemigrations
```

```bash
python ./manage.py migrate
```

To Create a super user, use the following command and set email and password accordingly which will be used to log into the admin dashboard.

```bash
python ./manage.py createsuperuser
```

Now we can successfully start the backend server

```bash
python ./manage.py runserver
```

#### Installing the requirements for the `frontend`.

In a new terminal, change directory to the extension folder using following command:

```bash
cd halt-ai
```

Install the necessary packages to build the extension using the command:

```bash
npm install -g pnpm
```

```bash
pnpm install
```

Now open the file `<PROJECT_FOLDER>\halt-ai\src\utils\handler.ts` in any code editor of preference and replace the variable value for `this.BASE_URL = '<ngrok-url-for-backend>'`.
Now we will compile the extension using the command:

```bash
pnpm build
```

This will create us a build of extension which could be installed inside the chrome extensions.

## Usage

### Usage of the Extension by Employee

Now go to `Manage Chrome Extension` page and **turn on** the `Developer Mode`

Click on the Load unpacked option and select the following folder `<PROJECT_FOLDER>\halt-ai\build\chrome-mv3-prod`

Now go to the options panel of the extension by using right click on the extension on the top right and clicking on the options tab.

This will show a window to Login using the Employee ID. Type in the ID of the Employee. This will be used for logging in the administration panel.

#### Using the extension on `ChatGPT` or `Gemini`

The extension automatically activates when the user visits the following Generative AI Chatbots.
User will just have to write the query and press `Enter` to start the checking process, if the query is safe, the extension will automatically pass the request to the chatbots to proceed and if not safe then will not allow the request and show the error on the screen of the user.

### Usage of Admin Panel by the Administrator

Admin can visit the administration panel by using the following link in the browser:

```url
https://127.0.0.1:8000/admin
```

## Testing

The testing folder contains Jupyter Notebook `testing.ipynb` which was used to test the API with 113 different queries stored in the `Book1.xlsx` file inside the folder.

## Query

For any query, feel free to react out to [Siddharth Agrawal](mailto:agrawalsiddharth329@gmail.com?subject=Halt.AI%20Help%20%for%Installation) on `agrawalsiddharth329@gmail.com`
