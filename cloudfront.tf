resource "aws_cloudfront_distribution" "api_dist" {
    origin {
        domain_name = data.aws_cloudformation_stack.sam.outputs["DemoApi"]
        origin_id = "sam-api-gateway"

        custom_origin_config {
            https_port = 443
            http_port = 80
            origin_protocol_policy = "https-only"
            origin_ssl_protocols = ["TLSv1.2"]
        }
    }

    enabled = true
    default_cache_behavior {
        allowed_methods = ["GET", "HEAD"]
        cached_methods = ["GET", "HEAD"]
        target_origin_id = "sam-api-gateway"

        forwarded_values {
            query_string = true
            cookies {
                forward = "none"
            }
        }

        viewer_protocol_policy = "https-only"
        min_ttl = 0
        default_ttl = 3600
        max_ttl = 86400
    }

    restrictions {
        geo_restriction {
            restriction_type = "whitelist"
            locations = ["JP"]
        }
    }

    viewer_certificate {
        cloudfront_default_certificate = true
    }
}

