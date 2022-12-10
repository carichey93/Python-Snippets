def create_daily_report(df):
    """
    Example of writing a pandas data frame and writing/formatting individual cells in Excel
    """
    # Create new file from summary_template.xlsx
    output_excel_file = os.path.join(OUTPUT_DIR, OUTPUT_NAME + ".xlsx")
    template = os.path.join(os.path.dirname(__file__), "summary_template.xlsx")
    shutil.copyfile(template, output_excel_file)

    # Write data frame to the created Excel file (Summary sheet on row 12)
    with pd.ExcelWriter(
            output_excel_file,
            mode="a",
            engine="openpyxl",
            if_sheet_exists="overlay",
    ) as writer:
        df.to_excel(
            writer, sheet_name="Summary", startrow=12, index=False, header=False
        )
        ws = writer.sheets["Summary"]
        ws["A9"] = END_DATE.date()

        # Adjust time formatting now - will not work to adjust formatting of template
        for cell in ws["E13:F24"]:
            cell[0].number_format = "hh:mm AM/PM"
            cell[1].number_format = "hh:mm AM/PM"
