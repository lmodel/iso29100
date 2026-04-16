package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Schema class documenting a PII processing operation: its purpose, legal basis, operation types performed, categories of PII involved, responsible actors, applied controls, retention period, and any cross-border transfer safeguards.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PIIProcessingActivity extends NamedEntity {

  private String processingPurpose;
  private String legalBasis;
  private List<String> operationsPerformed;
  private List<String> piiCategoriesProcessed;
  private List<String> sensitivityLevelsInvolved;
  private PIIController controllerRef;
  private PIIProcessor processorRef;
  private List<PIIFlowScenario> dataFlows;
  private String retentionPeriod;
  private List<PrivacyControl> privacyControlsApplied;
  private boolean crossBorderTransfer;
  private List<String> transferSafeguards;

}