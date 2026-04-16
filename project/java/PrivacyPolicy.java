package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Schema class for a governing document expressing an organization's intentions and commitments for PII processing. Covers both the internal policy document and any external privacy notice made available to PII principals (referred to as a notice in this framework).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PrivacyPolicy extends NamedEntity {

  private String policyVersion;
  private LocalDate effectiveDate;
  private String policyScope;
  private List<String> processingPurposesCovered;
  private List<String> piiCategoriesCovered;
  private String dataRetentionStatement;
  private List<String> piiPrincipalRights;
  private String contactForInquiries;
  private LocalDate lastReviewDate;
  private boolean isExternalNotice;
  private List<String> applicablePrinciples;

}