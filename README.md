# Online supplement to Explainable PCA Decomposition of Player Features for Football Profiling

---

## Setup guide

Follow these steps to set up your project with Python package manager - uv:

1. **Install uv**

   Choose one of the following installation methods. For more installation options, refer to the [uv installation documentation](https://github.com/astral-sh/uv/blob/main/docs/getting-started/installation.md).

   - **Standalone Installer:**

     For macOS and Linux:
     ```sh
     curl -LsSf https://astral.sh/uv/install.sh | sh
     ```

   -  **For Windows:**

      ```powershell
       powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
      ```


   - **Using pip:**
     ```sh
     pip install uv
     ```

   - **Using pipx:**
     ```sh
     pipx install uv
     ```

2. **Clone the Repository**

   Replace `<repository_url>` with your repository's URL:

   ```sh
   git clone <repository_url>
   cd <repository_name>
   ```

3. **Synchronize Dependencies**

   In the project directory, run:

   ```sh
   uv sync
   ```

   This command will install all necessary dependencies as specified in `pyproject.toml` and `uv.lock` files.

4. **All set!**
   You should be able to run all notebooks without any issues