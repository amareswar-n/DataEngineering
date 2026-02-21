@echo off
for /d %%d in (*) do (
    (
        echo # %%d
        echo.
        echo Notes:
        echo.
        echo Projects:
        echo.
        echo Resources:
    ) > "%%d\README.md"
)