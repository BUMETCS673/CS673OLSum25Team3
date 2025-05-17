# GetActive Frontend Project

## Development Instructions

### Setup Devcontainer
1. Install [VSCode IDE](https://code.visualstudio.com/Download) then install `Dev Containers` extension.
2. Launch VSCode IDE, click on `File -> Open Folder`, then select `frontend` folder.
3. Type `Dev Containers: Reopen in Container` command.

Once devcontainer finished its configurations, you are now ready for development.
For developer:

### Install Dependencies
Type below commonds in the terminal:
```bash
npm install
```

### Start Development Server
Type below commonds in the terminal:
```bash
npm run dev
```

### Other available Commonds
Type below commonds in the terminal:
```bash
npm run lint #Run ESLint to check code quality 
npm run test #Run tests
```

### Project Structure
```
src/
├── components/   # Reusable components
├── pages/        # Page components
├── hooks/        # Custom React Hooks
├── services/     # API services and data fetching
├── tests/            # All test files
    ├── components/
    │   ├── Button.test.jsx
    │   └── ...
    ├── pages/
    │   ├── Home.test.jsx
    │   └── ...
    └── utils/
        ├── format.test.js
        └── ...
├── utils/        # Utility functions
└── App.jsx       # Application entry component
```

### Debugging
Use browser developer tools or React DevTools for debugging. 