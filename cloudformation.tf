resource "aws_cloudformation_stack" "sam" {
    name = "sam"
    template_body = file("template.yaml")
    capabilities = ["CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
    parameters = {
        "TableName" = "demo"
    }
}

data "aws_cloudformation_stack" "sam" {
    name = "sam"
    depends_on = [
        aws_cloudformation_stack.sam
    ]
}

